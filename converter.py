import json
import sys

# Check if the user has provided a filename as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python script_name.py <chat_file.json>")
    sys.exit(1)

# Get the chat file name from the command-line arguments
chat_file_name = sys.argv[1]

try:
    # Load the specified JSON chat export
    with open(chat_file_name, 'r') as f:
        chat_data = json.load(f)

    # Create the Markdown output file based on the input filename
    output_md_file = chat_file_name.replace('.json', '_summary.md')

    with open(output_md_file, 'w') as md_file:
        # Write a title for the summary
        md_file.write("# Chat Summary\n\n")

        # Extracting request and responses
        for request in chat_data['requests']:
            request_message = request['message']['text']
            md_file.write(f"**User Request:**\n\n{request_message}\n\n")

            for response in request['response']:
                if 'value' in response:
                    response_message = response['value']
                    md_file.write(f"**GitHub Copilot Response:**\n\n{response_message}\n\n")

                # Check if there are any tool invocation steps
                if 'toolInvocationSerialized' in response:
                    tool_message = response['toolInvocationSerialized']['invocationMessage']['value']
                    md_file.write(f"**Tool Invocation Message:**\n\n{tool_message}\n\n")

                # Check if there are results embedded
                if 'resultDetails' in response and 'output' in response['resultDetails']:
                    for output in response['resultDetails']['output']:
                        if 'value' in output:
                            md_file.write(f"**Tool Output:**\n\n{output['value']}\n\n")

    print(f"Chat summary converted to Markdown and saved as {output_md_file}")

except FileNotFoundError:
    print(f"Error: The file {chat_file_name} does not exist.")
except json.JSONDecodeError:
    print(f"Error: The file {chat_file_name} is not a valid JSON file.")
