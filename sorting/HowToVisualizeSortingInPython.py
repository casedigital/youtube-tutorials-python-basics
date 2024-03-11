# How to Visualize sorting in python?

import matplotlib.animation as animation
import matplotlib.pyplot as plt


def selection_sort(arr):
    len_arr = len(arr)

    for i in range(len_arr):
        min_idx = i
        for j in range(i + 1, len_arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # print(f'before: {arr}')
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # print(f'  after: {arr}')
        yield arr.copy(), i, min_idx
    # return arr


def init_plot(arr):
    fig, ax = plt.subplots()
    ax.set_title("Visualized Sorting")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 10)

    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    return fig, ax, bars


def update_plot_selection_sort(frame, bars, arr):
    arr_data, current_idx, min_idx = arr[frame]
    for i, (bar, val) in enumerate(zip(bars, arr_data)):
        if i == current_idx:
            bar.set_color('red')
        elif i == min_idx:
            bar.set_color('green')
        else:
            bar.set_color('skyblue')

        bar.set_height(val)
    return bars


if __name__ == "__main__":
    cur_list = [33, 7, 4, 5, 20, 1, 44, 2, 9, 10, 21]
    print(f"Unordered: {cur_list = }")

    sel_sort_arr = selection_sort(cur_list.copy())
    # print(f"Ordered: {sel_sort_arr = }")
    fig, ax, bars = init_plot(cur_list)

    ani = animation.FuncAnimation(
        fig,
        update_plot_selection_sort,
        frames=len(cur_list),
        fargs=(bars, list(sel_sort_arr)),
        interval=500,
        repeat=True
    )

    plt.show()