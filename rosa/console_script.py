#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from os import path
import create_workspace
import merge_rosinstall

def get_parser():
    parser = argparse.ArgumentParser(description='Helpful commands for performing common ROS tasks.')
    subparsers = parser.add_subparsers()

    create_workspace.add_parser(subparsers)
    merge_rosinstall.add_parser(subparsers)
    return parser

def main():
    args = get_parser().parse_args()
    args.func(args)