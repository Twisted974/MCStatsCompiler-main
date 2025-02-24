import excel2img

# Save as PNG the range of used cells in test.xlsx on page named "Sheet1"
excel2img.export_img("output.xlsx", "../images/outputGlobal.png", "Global", None)
excel2img.export_img("output.xlsx", "../images/outputShiny.png", "Shiny", None)
