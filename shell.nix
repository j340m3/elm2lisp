{
  pkgs ? import <nixpkgs> { },
}:
#useless comment
pkgs.mkShell {
  nativeBuildInputs = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.tree-sitter-grammars.tree-sitter-elm
      python-pkgs.tree-sitter
      python-pkgs.hy
    ]))
  ];
}
