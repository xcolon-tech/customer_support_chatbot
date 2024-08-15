# Social Media Scheduling Tool
Hosts Server Django Application for Social Media Scheduling Tool

# User Registration
curl -X POST http://127.0.0.1:8000/api/user/register/ \
-H "Content-Type: application/json" \
-d '{
    "username": "user1",
    "mobile": "1234567890",
    "mpin": "1234",
    "password": "strongpassword"
}'

# User Login
curl -X POST http://127.0.0.1:8000/api/user/login/ \
-H "Content-Type: application/json" \
-d '{
    "mobile": "1234567890",
    "mpin": "1234"
}'

# Fetch chat history
curl -X GET http://127.0.0.1:8000/api/chat/history/ \
-H "Authorization: Token your_token"

# Send Message
curl -X POST http://127.0.0.1:8000/api/chat/send/ \
-H "Authorization: Token your_token" \
-H "Content-Type: application/json" \
-d '{"receiver": "bot", "message": "Hello Bot"}'

# Get User Settings
curl -X GET http://127.0.0.1:8000/api/settings/user/ \
-H "Authorization: Token your_token"

# Update User Settings
curl -X PATCH http://127.0.0.1:8000/api/settings/user/ \
-H "Authorization: Token your_token" \
-H "Content-Type: application/json" \
-d '{"default_language": "ES", "automated_response": false}'

# Upload Profile Picture
curl -X PATCH http://127.0.0.1:8000/api/settings/upload-profile-picture/ \
-H "Authorization: Token your_token" \
-H "Content-Type: multipart/form-data" \
-F "bot_profile_picture=@/path/to/your/image.png"

# User Logout
curl -X POST http://127.0.0.1:8000/api/disconnect/logout/ \
-H "Authorization: Token your_token"