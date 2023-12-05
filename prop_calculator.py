class Hat:
  def __init__(self, **balls):
      # convert arguments to contents list
      self.contents = []
      for color, quantity in balls.items():
          self.contents.extend([color] * quantity)

  def draw(self, num_balls):
      # draw balls at random without replacement
      drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
      for ball in drawn_balls:
          self.contents.remove(ball)
      return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # perform experiments and estimate probability
  successful_experiments = 0

  for _ in range(num_experiments):
      # copy the hat to avoid modifying the original
      hat_copy = Hat()
      hat_copy.contents = hat.contents.copy()

      # draw balls from the hat
      drawn_balls = hat_copy.draw(num_balls_drawn)

      # check if the drawn balls match the expected ones
      drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}
      if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
          successful_experiments += 1

  # calculate and return the probability
  probability = successful_experiments / num_experiments
  return probability
