with open('kusto_result') as f:
    content = f.read().splitlines()

finalContent = '|'.join(content)

print(finalContent)