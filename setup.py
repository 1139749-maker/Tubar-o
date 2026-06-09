import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(
                   script="main.py", 
                   icon="bases/icone.ico",
                    target_name="NadeSePuder.exe"
                   ) ]
cx_Freeze.setup(
    name = "Nade Se Puder",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["bases","recursos"]
        }
    }, executables = executaveis
)
