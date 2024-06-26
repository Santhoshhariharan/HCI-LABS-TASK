
## Installation

1. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

2. Set up your OpenAI API key:

    - Sign up for an account at [OpenAI](https://openai.com).
    - Obtain your API key from the dashboard.
    - Set your API key as an environment variable named `OPENAI_API_KEY`.

## Usage

### Training

To train the TensorFlow model, use the `train.py` script:

```bash
python train.py
```

This script will train the model using the provided dataset.

### Testing

To test the trained model, use the `test.py` script:

```bash
python test.py
```

This script will evaluate the performance of the model on a test dataset.

### Running the ChatGPT API

To run the ChatGPT API powered by OpenAI, use the `chatgpt_api_powered.py` script:

```bash
python chatgpt_api_powered.py
```

This script will start the API server, allowing you to interact with the ChatGPT model via HTTP requests.

## Credits

This project is maintained by Santhosh.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


