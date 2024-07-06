import datetime


def save_markdown(task_output):
    result_content = task_output.result if isinstance(task_output.result, str) else str(task_output.result)

    today_date = datetime.now().strftime('%Y-%m-%d')
    filename = f"{today_date}.md"
    with open(filename, 'w') as file:
        file.write(result_content)
        print(f"Markdown saved as {filename}")