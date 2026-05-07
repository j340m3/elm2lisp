{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell import ./extracted-attrs.nix { inherit pkgs; }