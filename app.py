<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fake News Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f0f0f0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: 100vh;
            padding-top: 50px;
            margin: 0;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        textarea {
            width: 80%;
            max-width: 500px;
            height: 120px;
            padding: 10px;
            font-size: 16px;
            margin-bottom: 10px;
            resize: vertical;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            margin: 5px;
        }
        #result {
            margin-top: 20px;
            font-size: 22px;
            font-weight: bold;
        }
        .sample-buttons {
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <h1>Fake News Detector</h1>
    <textarea id="newsText" placeholder="Paste news here..."></textarea><br>
    <button onclick="checkNews()">Check</button>

    <div class="sample-buttons">
        <button onclick="checkSample('Breaking: Shocking clickbait story!')">Test Fake</button>
        <button onclick="checkSample('Local community garden opens today')">Test Real</button>
    </div>

    <div id="result"></div>

    <script>
        async function checkNews() {
            const news = document.getElementById('newsText').value.trim();
            const resultDiv = document.getElementById('result');

            if(news === "") {
                resultDiv.innerText = "Please enter some news text!";
                resultDiv.style.color = "black";
                return;
            }

            try {
                const response = await fetch("https://fake-news-app-78v7.onrender.com/predict", { 
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ news: news })
                });

                console.log("Response received:", response);
                const data = await response.json();
                console.log("Data:", data);

                if(data.result === "Fake") {
                    resultDiv.innerText = "Result: Fake";
                    resultDiv.style.color = "red";
                } else if(data.result === "Real") {
                    resultDiv.innerText = "Result: Real";
                    resultDiv.style.color = "green";
                } else {
                    resultDiv.innerText = "Unexpected response from API";
                    resultDiv.style.color = "orange";
                }
            } catch (err) {
                resultDiv.innerText = "Error connecting to API!";
                resultDiv.style.color = "orange";
                console.error(err);
            }
        }

        function checkSample(text) {
            document.getElementById('newsText').value = text;
            checkNews();
        }
    </script>
</body>
</html>

