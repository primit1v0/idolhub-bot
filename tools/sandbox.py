import shlex
import os
from pathlib import Path

def wrap_bwrap(command: str, workspace: str, cwd: str) -> str:
    """
    Membungkus command dalam bubblewrap sandbox (membutuhkan 'bwrap' terinstall di host).
    """
    ws = Path(workspace).resolve()
    
    # Validasi CWD agar tidak bisa kabur dari workspace
    try:
        sandbox_cwd = str(ws / Path(cwd).resolve().relative_to(ws))
    except ValueError:
        # Jika CWD berada di luar workspace, paksa kembali ke root workspace
        sandbox_cwd = str(ws)

    required = ["/usr"]
    optional = ["/bin", "/lib", "/lib64", "/etc/alternatives", 
                "/etc/ssl/certs", "/etc/resolv.conf", "/etc/ld.so.cache"]

    args = [
        "bwrap", 
        "--new-session", 
        "--die-with-parent", 
        "--unshare-all", 
        "--share-net",
        "--clearenv",
        "--setenv", "PATH", "/usr/local/bin:/usr/bin:/bin",
        "--setenv", "HOME", str(ws),
        "--setenv", "USER", "sandbox",
        "--setenv", "LOGNAME", "sandbox",
        "--setenv", "SHELL", "/bin/sh",
    ]
    
    for p in required:
        args += ["--ro-bind", p, p]
    for p in optional:
        args += ["--ro-bind-try", p, p]

    # Kita timpa parent dir (misal: /opt) dengan tmpfs kosong
    # Supaya idolhub config dan source code tidak terlihat
    parent_dir = str(ws.parent)

    args += [
        "--proc", "/proc",
        "--dev", "/dev",
        "--tmpfs", "/tmp",
        "--tmpfs", parent_dir,           # Sembunyikan parent directory
        "--dir", str(ws),                # Buat mount point workspace baru
        "--bind", str(ws), str(ws),      # Mount workspace RW
        "--chdir", sandbox_cwd,          # Atur working directory
        "--", "sh", "-c", command
    ]

    return shlex.join(args)
