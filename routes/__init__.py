from .student import students_bp  # Import the blueprint from students.py

# Expose the blueprints so they can be registered in the main app
__all__ = ['students_bp']