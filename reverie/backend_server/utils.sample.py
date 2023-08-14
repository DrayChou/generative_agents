# default config
openai_api_type = None # azure or chatglm or openai or None
openai_api_key = None
openai_api_base = None
openai_api_model = None
openai_api_engine = None
openai_api_version = None

# Copy and paste your OpenAI API Key
openai_api_key = ""
openai_api_base = None
openai_api_model = "gpt-3.5-turbo"

# local One-api
# openai_api_type = "oneapi"
# openai_api_key = "token1"
# openai_api_base = "http://10.10.0.7:9096/v1"
# openai_api_model ="chinese-llama-alpaca-2"

# local chatglm-6b
# openai_api_type = "chatglm"
# openai_api_key = "token1"
# openai_api_base = "http://10.10.0.7:9092/v1"
# openai_api_model ="chatglm2-6b"

# azure config
# openai_api_type = "azure" # azure or openai
# openai_api_version = "2023-05-15"
# openai_api_engine = "gpt-35-turbo"
# openai_api_key = ""
# openai_api_base = ""

# openai proxy
proxies = None
# proxies = {
#     "http": "http://127.0.0.1:7893",
#     "https": "http://127.0.0.1:7893",
# }

# Put your name
key_owner = "Dray"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True