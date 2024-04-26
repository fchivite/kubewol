from webconsole import create_app, create_database
app_port = 5000

app = create_app()
#db = create_database(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(app_port), debug=True)
	
