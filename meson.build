project(
  'ecvt',
  'cpp',
  version : '0.1',
  default_options : [
    'warning_level=3',
    'cpp_std=c++20'
    ]
  )

phoenixlib = declare_dependency(
  link_args: ['-L../lib/raspberry', '-l:libCTRE_Phoenix.so', '-l:libCTRE_PhoenixCCI.so'],
  include_directories: include_directories('include')
  )

executable(
  'ecvt',
  'src/main.cpp',
  dependencies: [phoenixlib]
  )
