import subprocess
import asyncio

# result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# if result.returncode == 0:
#     print("Command executed successfully")
#     print("Output:", result.stdout)
# else:
#     print("Error:", result.stderr)


async def linux_process():
    command = "cd ui && npm run dev"
    # command = "cd ui && npm install && npm run build && npm start"

    process = await asyncio.create_subprocess_shell(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    async for line in process.stdout:
        print(line.strip())

    stderr = await process.stderr.read()
    if stderr:
        print("Error:", stderr.strip())
