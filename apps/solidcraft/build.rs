#![forbid(unsafe_code)]

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let icon = std::path::Path::new(env!("CARGO_MANIFEST_DIR")).join("../../assets/icons/app/windows/exports/solidcraft-executable.ico");
    println!("cargo:rerun-if-changed={}", icon.display());
    println!("cargo:rerun-if-changed=build.rs");
    if std::env::var("CARGO_CFG_TARGET_OS")? != "windows" {
        return Ok(());
    }
    let out = std::path::PathBuf::from(std::env::var_os("OUT_DIR").ok_or("missing OUT_DIR")?);
    let copy = out.join("solidcraft.ico");
    if let Err(e) = std::fs::copy(&icon, &copy) {
        println!("cargo:warning=failed to copy icon: {e}");
        return Ok(());
    }
    let rc = out.join("solidcraft.rc");
    let _ = std::fs::write(&rc, "1 ICON \"solidcraft.ico\"\n");
    if let Err(e) = embed_resource::compile_for(&rc, ["solidcraft"], embed_resource::NONE).manifest_required() {
        println!("cargo:warning=failed to embed resource icon: {e}");
    }
    Ok(())
}
