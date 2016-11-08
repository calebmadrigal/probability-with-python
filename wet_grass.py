# Probability that the sprinkler is on given that the grass is wet
import random

def get_rain():
    return random.random() <= 0.2

def get_sprinkler(rain):
    if rain:
        return random.random() <= 0.01
    else:
        return random.random() <= 0.4

def get_grass_wet(sprinkler, rain):
    if sprinkler and rain:
        return random.random() <= 0.99
    elif sprinkler and not rain:
        return random.random() <= 0.9
    elif not sprinkler and rain:
        return random.random() <= 0.8
    elif not sprinkler and not rain:
        return random.random() <= 0.0

def rejection_sampling(num_samples=10000000):
    sprinkler_given_grass_wet = 0
    num_grass_wet = 0
    for i in range(num_samples):
        rain = get_rain()
        sprinkler = get_sprinkler(rain)
        grass_wet = get_grass_wet(sprinkler, rain)
        #print('Sample: {}, R={}, S={}, G={}'.format(i, rain, sprinkler, grass_wet))

        # Only consider samples where the grass is wet
        if grass_wet:
            num_grass_wet += 1
            if sprinkler:
                sprinkler_given_grass_wet += 1

    return sprinkler_given_grass_wet / num_grass_wet

print('RESULT: {}'.format(rejection_sampling()))
