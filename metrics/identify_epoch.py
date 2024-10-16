import re
import random

def parse_log_file(log_file_path):
    epoch_losses = {}
    with open(log_file_path, 'r') as file:
        for line in file:
            match = re.search(r'Epoch:\s*(\d+)/\s*\d+\|\s*Iteration:\s*\d+\|\s*Loss:(\d+\.\d+)', line)
            if match:
                epoch = int(match.group(1))
                loss = float(match.group(2))
                if epoch not in epoch_losses:
                    epoch_losses[epoch] = []
                epoch_losses[epoch].append(loss)
    return epoch_losses

def find_best_epoch(epoch_losses):
    best_epoch = None
    best_loss = float('inf')
    for epoch, losses in epoch_losses.items():
        avg_loss = sum(losses) / len(losses)
        if avg_loss < best_loss:
            best_loss = avg_loss
            best_epoch = epoch
    return best_epoch, best_loss

def find_worst_epoch(epoch_losses):
    worst_epoch = None
    worst_loss = float('-inf')
    for epoch, losses in epoch_losses.items():
        avg_loss = sum(losses) / len(losses)
        if avg_loss > worst_loss:
            worst_loss = avg_loss
            worst_epoch = epoch
    return worst_epoch, worst_loss

def find_random_epoch(epoch_losses):
    random_epoch = random.choice(list(epoch_losses.keys()))
    avg_loss = sum(epoch_losses[random_epoch]) / len(epoch_losses[random_epoch])
    return random_epoch, avg_loss

if __name__ == "__main__":
    log_file_path = '/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/log_test.txt'
    epoch_losses = parse_log_file(log_file_path)
    
    best_epoch, best_loss = find_best_epoch(epoch_losses)
    worst_epoch, worst_loss = find_worst_epoch(epoch_losses)
    random_epoch, random_loss = find_random_epoch(epoch_losses)

    print(f"Best epoch: {best_epoch} with average loss: {best_loss:.6f}")
    print(f"Worst epoch: {worst_epoch} with average loss: {worst_loss:.6f}")
    print(f"Random epoch: {random_epoch} with average loss: {random_loss:.6f}")

    # save the result to a file
    with open('/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/epoch_results.txt', 'w') as f:
        f.write(f"Best epoch: {best_epoch} with average loss: {best_loss:.6f}\n")
        f.write(f"Worst epoch: {worst_epoch} with average loss: {worst_loss:.6f}\n")
        f.write(f"Random epoch: {random_epoch} with average loss: {random_loss:.6f}\n")
