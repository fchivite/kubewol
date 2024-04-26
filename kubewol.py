from webconsole import create_app
app_port = 5000

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(app_port), debug=True)
	
