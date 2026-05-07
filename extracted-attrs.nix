{ pkgs, ... }:
{
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.tree-sitter-grammars.tree-sitter-elm
      python-pkgs.tree-sitter
      python-pkgs.hy
    ]))
  ];
}
