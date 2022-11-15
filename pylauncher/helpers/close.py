import psutil


def close(list: list[dict[str, dict[str, dict[str, str | list[str]]]]]) -> None:
    '''
    Closes programs from list
    '''

    for program in list:
        # Get program path
        p = str(program["path"])

        # Remove path and get program name
        programName = p.split("\\")[-1]

        # Remove extension from name
        cleanName = programName.rsplit(".", 1)[0]

        for process in (process for process in psutil.process_iter() if process.name().startswith(cleanName)):
            process.kill()
