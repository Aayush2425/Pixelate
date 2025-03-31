from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    full_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=['student', 'mentor', 'admin'], default='student')
    preferred_language = serializers.CharField(max_length=50, default='en')
    created_at = serializers.DateTimeField(read_only=True)

class CourseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.UUIDField(required=False)  
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField(max_length=100), required=False)
    languages = serializers.ListField(child=serializers.CharField(max_length=50), required=True)
    difficulty_level = serializers.ChoiceField(choices=['beginner', 'intermediate', 'advanced'])
    created_at = serializers.DateTimeField(read_only=True)

class LessonSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    course_id = serializers.UUIDField()
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    video_url = serializers.URLField(required=False, allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)
    # hello

class ExerciseSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    lesson_id = serializers.UUIDField()
    description = serializers.CharField()
    starter_code = serializers.CharField(required=False, allow_blank=True)
    difficulty = serializers.ChoiceField(choices=['easy', 'medium', 'hard'])
    created_at = serializers.DateTimeField(read_only=True)

class SubmissionSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.UUIDField()
    exercise_id = serializers.UUIDField()
    code = serializers.CharField()
    ai_feedback = serializers.CharField(required=False, allow_blank=True)
    passed_tests = serializers.BooleanField(default=False)
    submitted_at = serializers.DateTimeField(read_only=True)

class QuizQuestionSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    course_id = serializers.UUIDField()
    question_text = serializers.CharField()
    options = serializers.JSONField()
    correct_answer = serializers.CharField()
    explanation = serializers.CharField(required=False, allow_blank=True)

class UserProgressSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.UUIDField()
    course_id = serializers.UUIDField()
    completed_lessons = serializers.IntegerField(default=0)
    completed_exercises = serializers.IntegerField(default=0)
    last_active = serializers.DateTimeField(read_only=True)

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.UUIDField()
    score = serializers.IntegerField(default=0)
    ranking = serializers.IntegerField(required=False, allow_null=True)

class FeedbackSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    user_id = serializers.UUIDField()
    course_id = serializers.UUIDField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comments = serializers.CharField(required=False, allow_blank=True)
    likes = serializers.IntegerField(default=0, min_value=0, required=False)
    dislikes = serializers.IntegerField(default=0, min_value=0, required=False)
    created_at = serializers.DateTimeField(read_only=True)
