

def user_test_nivel_one(user):
	"""
		Valida si el usuario es de nivel 1

	"""
	if user.profile:
		return user.profile.permiso == 1

	return False