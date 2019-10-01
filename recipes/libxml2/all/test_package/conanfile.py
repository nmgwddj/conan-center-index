#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        arg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "books.xml"))
        bin_arg_path = "%s %s" % (bin_path, arg_path)
        self.run(bin_arg_path, run_environment=True)
