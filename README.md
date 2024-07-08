
# Facebook Posts Sentiment Analysis

This project analyzes the sentiment of your Facebook posts and visualizes the results using a histogram.

## How It Works

1. **Connect to Facebook:**
   - The code connects to the Facebook Graph API using an access token to access your Facebook data.

2. **Fetch Your Posts:**
   - It retrieves posts from your Facebook profile.

3. **Save Posts to a File:**
   - The posts are saved into a file named `posts.json`.

4. **Load Posts from the File:**
   - The code reads the `posts.json` file to load the posts back into the program for further processing.

5. **Preprocess Text:**
   - Each post's text is cleaned by removing special characters and converting all letters to lowercase.

6. **Perform Sentiment Analysis:**
   - The cleaned-up text is analyzed to determine its sentiment, indicating whether the text is positive, negative, or neutral.

7. **Visualize Results:**
   - A histogram is created to show the distribution of sentiment scores, helping visualize the overall sentiment of your posts.

## Requirements

- Python 3.x
- `facebook-sdk`
- `textblob`
- `matplotlib`


## Usage

1. Set your Facebook access token in the code:
   ```python
   access_token = "YOUR_USER_ACCESS_TOKEN"
   ```

2. Run the script:
   ```sh
   python script_name.py
   ```

3. The script will:
   - Fetch your Facebook posts
   - Save them to `posts.json`
   - Load the posts from `posts.json`
   - Preprocess and analyze the text for sentiment
   - Display a histogram of the sentiment analysis results

## Notes

- Ensure you have the required permissions (`user_posts`) for the access token to fetch your posts.
- The access token must be kept secure and should not be shared publicly.

## Example

Here's an example of how the histogram might look:

![Sentiment Analysis Histogram]

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides a clear and concise explanation of how the project works, the requirements, installation steps, usage instructions, and an example output. Make sure to replace `"YOUR_USER_ACCESS_TOKEN"` with your actual access token and update the repository URL and script name accordingly.
