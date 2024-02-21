 <h1>YouTube Video Downloader</h1>

    <p>A simple web application for downloading YouTube videos by providing the video link. The application is built
        using Django Rest Framework for the backend and React for the frontend. It utilizes the Pytube library for
        handling YouTube video downloads in the backend.</p>

    <h2>Table of Contents</h2>

    <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#tech-stack">Tech Stack</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#api-endpoints">API Endpoints</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2>Features</h2>

    <ul>
        <li><strong>YouTube Video Download:</strong> Users can paste a YouTube video link and download the video in
            their preferred quality.</li>
        <li><strong>Responsive UI:</strong> The frontend is built using React to provide a responsive and user-friendly
            interface.</li>
    </ul>

    <h2>Tech Stack</h2>

    <ul>
        <li><strong>Backend:</strong> Django Rest Framework</li>
        <li><strong>Frontend:</strong> React</li>
        <li><strong>Database:</strong> SQLite (for simplicity, can be changed to a more robust database for production)
        </li>
        <li><strong>HTTP Requests:</strong> Axios</li>
        <li><strong>YouTube Video Download Library:</strong> Pytube</li>
    </ul>

    <h2>Installation</h2>

    <ol>
        <li>Clone the repository:</li>
    </ol>

    <pre><code>git clone https://github.com/your-username/youtube-video-downloader.git</code></pre>

    <ol start="2">
        <li>Navigate to the project directory:</li>
    </ol>

    <pre><code>cd youtube-video-downloader</code></pre>

    <!-- Continue the list with steps 3-8 -->

    <h2>Usage</h2>

    <ol>
        <li>Open the web application in your browser.</li>
        <li>Paste a YouTube video link in the provided input field.</li>
        <li>Choose the preferred video quality.</li>
        <li>Click the "Download" button to initiate the download.</li>
    </ol>

    <h2>API Endpoints</h2>

    <ul>
        <li><strong>GET /api/videos/:id:</strong> Get details of a specific video.</li>
        <li><strong>POST /api/videos:</strong> Add a new video for download.</li>
    </ul>

    <p>For more details on API usage, refer to the <a href="./API_DOCS.md">API documentation</a>.</p>

    <h2>Contributing</h2>

    <p>Contributions are welcome! Feel free to open issues or pull requests.</p>

    <h2>License</h2>

    <p>This project is licensed under the <a href="./LICENSE">MIT License</a>.</p>
