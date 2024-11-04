{
    description = "devFlake for soliprem.github.io";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system} = {
      default = pkgs.mkShell {
        buildInputs = with pkgs; [
          nushell
          hugo
        ];
        shellHook = ''
          export SHELL=${pkgs.nushell}/bin/nu
          exec nu
        '';
      };
    };
  };
}
