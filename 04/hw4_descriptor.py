class LinearRegression:
    '''Linear Regression model'''
    def __init__(self, karpaty_lr: float):
        self.karpaty_lr = karpaty_lr

    def __get__(self, instance, owner):
        '''get method for descriptor'''
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError('Empty value')

    def __set__(self, instance, lr):
        '''set method for descriptor'''
        if (isinstance(lr, float)
            and self.karpaty_lr == lr):
            instance.__dict__[self.name] = lr
        else:
            raise ValueError('Check hyperparameter')

    def __set_name__(self, name, owner):
        self.name = name


class RandomForest:
    '''Random Forest model'''
    def __init__(self, max_n_estimators: int, min_n_estimators: int):
        self.max_n_estimators = max_n_estimators
        self.min_n_estimators = min_n_estimators

    def __get__(self, instance, owner):
        '''get method for descriptor'''
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError('Empty value')

    def __set__(self, instance, n_estimators):
        '''set method for descriptor'''
        if (isinstance(n_estimators, int)
            and self.min_n_estimators <= n_estimators <= self.min_n_estimators):
            instance.__dict__[self.name] = n_estimators
        else:
            raise ValueError('Check hyperparameter')

    def __set_name__(self, name, owner):
        self.name = name


class KNN:
    '''K-nearest Neighbors model'''
    def __init__(self, n_neighbors_default):
        self.n_neighbors_default = n_neighbors_default

    def __get__(self, instance, owner):
        '''get method for descriptor'''
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        raise ValueError('Empty value')

    def __set__(self, instance, n_neighbors):
        '''set method for descriptor'''
        if (isinstance(n_neighbors, int)
            and n_neighbors == self.n_neighbors_default):
            instance.__dict__[self.name] = n_neighbors
        else:
            raise ValueError('Check hyperparameters')

    def __set_name__(self, name, owner):
        self.name = name


class MachineLearning:
    '''Machine Learning class'''
    linear_regression = LinearRegression(3e-4)
    random_forest = RandomForest(100, 500)
    knn = KNN(5)
    def __init__(self, linear_regression, random_forest, knn):
        self.linear_regression = linear_regression
        self.random_forest = random_forest
        self.knn = knn

    def __str__(self):
        return f'''Machine learning have model:
                \n\tLinear Regression with hyperparameter {self.linear_regression}
                \n\tRandom Forest with hyperparameter {self.random_forest}
                \n\tKNN with hyperparameter {self.knn}'''
