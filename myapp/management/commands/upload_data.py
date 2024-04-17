from ...models import Food
from django.core.management.base import BaseCommand

class Command(BaseCommand):
	help = 'Populate database with 50 most common foods'

	def handle(self, *args, **kwargs):
		foods_data = [
			{"name": "Apple", "carbs": 25, "protein": 0.5, "fats": 0.3, "calories": 95},
			{"name": "Chicken Breast", "carbs": 0, "protein": 31, "fats": 3.6, "calories": 165},
			{"name": "Banana", "carbs": 27, "protein": 1.3, "fats": 0.4, "calories": 105},
			{"name": "Broccoli", "carbs": 6, "protein": 2.8, "fats": 0.4, "calories": 55},
			{"name": "Salmon", "carbs": 0, "protein": 25, "fats": 13, "calories": 206},
			{"name": "White Rice", "carbs": 45, "protein": 4.3, "fats": 0.4, "calories": 205},
			{"name": "Ground Beef (80% lean)", "carbs": 0, "protein": 18, "fats": 20, "calories": 254},
			{"name": "Avocado", "carbs": 9, "protein": 2, "fats": 15, "calories": 160},
			{"name": "Egg", "carbs": 0.6, "protein": 6, "fats": 5, "calories": 78},
			{"name": "Almonds", "carbs": 6, "protein": 21, "fats": 49, "calories": 579},
			{"name": "Oatmeal", "carbs": 25, "protein": 6, "fats": 4, "calories": 145},
			{"name": "Spinach", "carbs": 1, "protein": 2.9, "fats": 0.4, "calories": 23},
			{"name": "Whole Wheat Bread", "carbs": 12, "protein": 3, "fats": 1, "calories": 69},
			{"name": "Sweet Potato", "carbs": 26, "protein": 1.6, "fats": 0.1, "calories": 112},
			{"name": "Greek Yogurt", "carbs": 6, "protein": 10, "fats": 0.4, "calories": 59},
			{"name": "Quinoa", "carbs": 21, "protein": 4, "fats": 2, "calories": 120},
			{"name": "Cottage Cheese", "carbs": 3.4, "protein": 11, "fats": 4.3, "calories": 98},
			{"name": "Carrots", "carbs": 10, "protein": 0.9, "fats": 0.2, "calories": 41},
			{"name": "Tuna", "carbs": 0, "protein": 29, "fats": 1, "calories": 128},
			{"name": "Peanut Butter", "carbs": 20, "protein": 25, "fats": 50, "calories": 588},
			{"name": "Milk", "carbs": 12, "protein": 8, "fats": 8, "calories": 150},
			{"name": "Black Beans", "carbs": 20, "protein": 7.6, "fats": 0.5, "calories": 110},
			{"name": "Blueberries", "carbs": 21, "protein": 1.1, "fats": 0.5, "calories": 84},
			{"name": "Pasta", "carbs": 25, "protein": 5, "fats": 0.5, "calories": 131},
			{"name": "Turkey Breast", "carbs": 0, "protein": 29, "fats": 1, "calories": 135},
			{"name": "Cheddar Cheese", "carbs": 1.3, "protein": 25, "fats": 33, "calories": 403},
			{"name": "Brown Rice", "carbs": 45, "protein": 4.5, "fats": 1.6, "calories": 216},
			{"name": "Green Beans", "carbs": 7, "protein": 1.8, "fats": 0.2, "calories": 31},
			{"name": "Beef Steak", "carbs": 0, "protein": 25, "fats": 15, "calories": 332},
			{"name": "Lentils", "carbs": 20, "protein": 9, "fats": 0.4, "calories": 116},
			{"name": "Oranges", "carbs": 15, "protein": 1.2, "fats": 0.2, "calories": 62},
			{"name": "Walnuts", "carbs": 4, "protein": 15, "fats": 65, "calories": 654},
			{"name": "Cucumber", "carbs": 3.6, "protein": 0.8, "fats": 0.1, "calories": 15},
			{"name": "Turkey Bacon", "carbs": 0, "protein": 17, "fats": 12, "calories": 197},
			{"name": "Bell Pepper", "carbs": 6, "protein": 1, "fats": 0.2, "calories": 31},
			{"name": "Pineapple", "carbs": 13, "protein": 0.5, "fats": 0.1, "calories": 50},
			{"name": "Soy Milk", "carbs": 7, "protein": 7, "fats": 4, "calories": 80},
			{"name": "Yogurt", "carbs": 4, "protein": 10, "fats": 3.3, "calories": 61},
			{"name": "Sunflower Seeds", "carbs": 20, "protein": 25, "fats": 51, "calories": 584},
			{"name": "Celery", "carbs": 3, "protein": 0.7, "fats": 0.2, "calories": 16},
			{"name": "Shrimp", "carbs": 0, "protein": 24, "fats": 0.3, "calories": 99},
			{"name": "Honey", "carbs": 82, "protein": 0.3, "fats": 0, "calories": 304},
			{"name": "Raspberries", "carbs": 12, "protein": 1.5, "fats": 0.8, "calories": 64},
			{"name": "Green Tea", "carbs": 0, "protein": 0, "fats": 0, "calories": 0},
			{"name": "Chickpeas", "carbs": 27, "protein": 9, "fats": 4.3, "calories": 164},
			{"name": "Mushrooms", "carbs": 3, "protein": 3.1, "fats": 0.3, "calories": 22},
			{"name": "Watermelon", "carbs": 8, "protein": 0.6, "fats": 0.2, "calories": 30},
		]

		for food_data in foods_data:
			Food.objects.create(**food_data)
