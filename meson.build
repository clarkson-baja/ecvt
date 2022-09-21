project('ecvt', 'cpp',
  version : '0.1',
)

lib_path = ''
if build_machine.cpu() == 'x86_64'
  lib_path = '../lib/x86-64'
else
  lib_path = '../lib/raspberry'
endif

phoenixlib = declare_dependency(
  link_args: ['-L'+lib_path, '-l:libCTRE_Phoenix.so', '-l:libCTRE_PhoenixCCI.so'],
  include_directories: include_directories('include')
)

executable('ecvt',
  'src/main.cpp',
  dependencies: [phoenixlib]
)
