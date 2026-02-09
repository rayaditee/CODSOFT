
# TASK 4 : SIMPLE RECOMMENDATION SYSTEM
# TECHNIQUE : CONTENT-BASED FILTERING


# Step 1: Movies and their features
movies = {
    "Inception": ["sci-fi", "thriller", "mind"],
    "Interstellar": ["sci-fi", "space", "drama"],
    "Titanic": ["romance", "drama"],
    "Avengers": ["action", "fantasy"],
    "Joker": ["psychological", "thriller"],
    "Gravity": ["space", "thriller"],
    "Notebook": ["romance", "emotional"]
}

# Step 2: User preferred features
user_likes = ["sci-fi", "space", "thriller"]

# Step 3: Calculate matching score
scores = {}

for movie, features in movies.items():
    match_count = 0
    for pref in user_likes:
        if pref in features:
            match_count += 1
    scores[movie] = match_count

# Step 4: Sort movies based on matching score
final_recommendation = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)

# Step 5: Display result
print("Recommended Items Based on Your Preferences:\n")

for movie, score in final_recommendation:
    if score > 0:
        print(movie, "→ Matching Score:", score)
