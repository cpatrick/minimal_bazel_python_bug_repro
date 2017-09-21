# Helpful macros to support requirements/pip integration.
git_repository(
    name = "io_bazel_rules_python",
    commit = "40d44a7258a9016925969e2ff41c93881ddd7155",
    remote = "https://github.com/bazelbuild/rules_python.git",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()

pip_import(
    name = "third_party_py",
    requirements = "//:requirements.txt",
)

load("@third_party_py//:requirements.bzl", "pip_install")

pip_install()
