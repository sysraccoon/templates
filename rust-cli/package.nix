{
  rustPlatform,
}:
rustPlatform.buildRustPackage {
  name = "{{ context.project_directory_name }}";
  src = ./.;

  cargoLock = {
    lockFile = ./Cargo.lock;
    allowBuiltinFetchGit = true;
  };
}
