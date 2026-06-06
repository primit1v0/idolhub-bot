import pytest
import os
from tools.sandbox import wrap_bwrap

def test_wrap_bwrap_formatting():
    command = "ls -la"
    workspace = "/tmp/fake_workspace"
    cwd = "/tmp/fake_workspace/subdir"
    
    wrapped = wrap_bwrap(command, workspace, cwd)
    
    # Harus pakai bwrap
    assert wrapped.startswith("bwrap --new-session")
    
    # Harus punya mount point wajib
    assert "--proc /proc" in wrapped
    assert "--dev /dev" in wrapped
    
    # Harus mem-bind workspace rw
    assert f"--bind {workspace} {workspace}" in wrapped
    
    # Harus men-tmpfs parent directory agar aman dari bocor path
    parent_dir = os.path.dirname(workspace)
    assert f"--tmpfs {parent_dir}" in wrapped
    
    # Harus execute shell command di akhir
    assert wrapped.endswith(f"-- sh -c 'ls -la'")
    
    # Chdir harus benar
    assert f"--chdir {cwd}" in wrapped

def test_wrap_bwrap_fallback_cwd():
    command = "pwd"
    workspace = "/tmp/fake_workspace"
    # CWD yang mencoba kabur dari workspace
    cwd = "/tmp/hack_the_system"
    
    wrapped = wrap_bwrap(command, workspace, cwd)
    
    # Sandbox harus memaksa CWD kembali ke workspace jika tidak match
    assert f"--chdir {workspace}" in wrapped
