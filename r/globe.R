num_obs <- 1000
p_grid <- seq(from=0, to=1, length.out=num_obs)
prob_p <- rep(1, num_obs)


prob_data <- dbinom(6, size=9, prob=p_grid)
posterior <- prob_data * prob_p
posterior_normalized = posterior / sum(posterior)
plot(posterior_normalized)