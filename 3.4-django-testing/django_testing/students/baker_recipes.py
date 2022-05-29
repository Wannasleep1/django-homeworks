from model_bakery import seq, baker
from model_bakery.recipe import Recipe

from students.models import Course


course_rec = Recipe(Course, name=seq("Course_", increment_by=1))
