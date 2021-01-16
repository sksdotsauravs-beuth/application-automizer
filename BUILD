load("@rules_python//python:defs.bzl", "py_binary", "py_test")
load("@pip//:requirements.bzl", "requirement")

# Toolchain setup, this is optional.
# Demonstrate that we can use the same python interpreter for the toolchain and executing pip in pip install (see WORKSPACE.bzl).
#
#load("@rules_python//python:defs.bzl", "py_runtime_pair")
#
#py_runtime(
#    name = "python3_runtime",
#    files = ["@python_interpreter//:files"],
#    interpreter = "@python_interpreter//:python_bin",
#    python_version = "PY3",
#    visibility = ["//visibility:public"],
#)
#
#py_runtime_pair(
#    name = "my_py_runtime_pair",
#    py2_runtime = None,
#    py3_runtime = ":python3_runtime",
#)
#
#toolchain(
#    name = "my_py_toolchain",
#    toolchain = ":my_py_runtime_pair",
#    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
#)
# End of toolchain setup.

py_binary(
    name = "app",
    srcs = [
        "app.py",
        "infrastructure/requirements_processor.py",
        "model/driver_info.py",
        "factory/driver_factory.py"
    ],
    data = glob([
        "*.txt"
    ]),
    deps = [
        requirement("beautifulsoup4"),
        requirement("selenium"),
    ]
)

py_test(
    name = "infrastructure_test",
    srcs = [
        "tests/infrastructure_test.py"
    ],
    deps = [":app"],
)