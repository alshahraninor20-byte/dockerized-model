from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from transformers import AutoModelForCausalLM, AutoTokenizer

TEAM = ["Wasan", "norah", "hura"]

MODEL_NAME = "Qwen/Qwen3-0.6B"

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto",
    device_map="auto"
)
print("Model loaded!")


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            message = "Team members: " + ", ".join(TEAM)
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(message.encode())

        elif self.path == "/generate":
            prompt = "Give me a short introduction to large language models."

            messages = [
                {"role": "user", "content": prompt}
            ]

            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False
            )

            model_inputs = tokenizer(
                [text],
                return_tensors="pt"
            ).to(model.device)

            generated_ids = model.generate(
                **model_inputs,
                max_new_tokens=100
            )

            output_ids = generated_ids[
                0
            ][len(model_inputs.input_ids[0]):].tolist()

            response = tokenizer.decode(
                output_ids,
                skip_special_tokens=True
            ).strip()

            result = {
                "prompt": prompt,
                "response": response
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps(result).encode()
            )

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8000), Server)

print("Server running on port 8000")
server.serve_forever()
