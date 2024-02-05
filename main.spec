# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('scripts/*', 'scripts'),
            ('static/data/*', 'static/data')],
    hiddenimports=[
        'scripts.arrange',
        'scripts.encrypt',
        'scripts.excuses',
        'scripts.intelligent',
        'scripts.mickey',
        'scripts.notes',
        'scripts.pomodoro',
        'scripts.session',
        'scripts.statistics',
        'scripts.tasks',
        'scripts.utils',
        'pyfiglet.fonts',
        'win10toast'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    datas=[('scripts/*', 'scripts'),
            ('static/data/*', 'static/data')], 
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
