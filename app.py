from flask import Flask, render_template, request,redirect
import youtube_dl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=["POST", "GET"])
def download():
    in_url = request.form['url']
    with youtube_dl.YoutubeDL() as ydl:
        new_url = ydl.extract_info(in_url, download=False)
        download_link = (new_url["formats"][-1]["url"])
        return redirect(download_link+"&dl=1")

if __name__ == '__main__':
    app.run(debug=True)