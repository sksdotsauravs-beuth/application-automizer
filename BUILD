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
    srcs = glob([
        "source/executor/*.py",
        "source/factory/*.py",
        "source/infrastructure/*.py",
        "source/model/*.py",
        "source/output/*.py",
        "source/pages/**/*.py",
        "source/pages/*.py",
        "source/utils/*.py",
        "source/validator/*.py",
        "source/*.py",
        "*.py"
    ]),
    data = glob([
        "resource/*.yml",
        "*.txt"
    ]),
    deps = [
        requirement("beautifulsoup4"),
        requirement("selenium"),
        requirement("pyyaml"),
        requirement("validators")
    ]
)

py_test(
    name = "library_version_test",
    srcs = [
        "tests/integration/library_version_test.py"
    ],
    deps = [":app"]
)

test_suite(
    name = "integration_tests",
    tests = [
        "library_version_test"
    ]
)

py_test(
    name = "requirements_reader_test",
    srcs = [
        "tests/infrastructure/requirements_reader_test.py"
    ],
    deps = [":app"]
)

py_test(
    name = "file_utils_test",
    srcs = [
        "tests/utils/file_utils_test.py"
    ],
    deps = [":app"]
)

test_suite(
    name = "unit_tests",
    tests = [
        "requirements_reader_test",
        "file_utils_test"
    ]
)