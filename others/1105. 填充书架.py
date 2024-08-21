from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        heights = []
        widths = []

        for i in range(N):
            width, height = books[i]
            widths.append(width)
            heights.append(height)


        records = {}
        def sub_min_height(current_height, books_ith, width_left, current_shelf_height) -> int:

            """
            1. ultimate we want sub_min_heigh(0,0, selfWidth, 0)

            2. if the current width left is not sufficiant then we have to 
            move to the next shelf

            3. if the current width left is enough for the current book, we have
            two options
                a. we keep this book in the shlef
                b. we move this book into next shelf


            """
            
            key = (current_height, books_ith, width_left, current_shelf_height)

            if key in records:
                return records[key]
            if books_ith >= N :
                records[key] = current_height 
                return current_height


            # we cannot keep this book
            if widths[books_ith] > width_left:

                result = sub_min_height(
                        current_height + heights[books_ith],
                        books_ith+1,
                        shelfWidth - widths[books_ith],
                        heights[books_ith]
                        )
                records[key] = result 
                return result

            else:
                # two options

                # a. we keep the book in the shelf
                height_gain = max(0, heights[books_ith] - current_shelf_height)
                we_keep = sub_min_height(
                        current_height + height_gain,
                        books_ith + 1,
                        width_left - widths[books_ith],
                        current_shelf_height + height_gain
                        )

                # b. we move on
                move_on = sub_min_height(
                        current_height + heights[books_ith],
                        books_ith + 1,
                        shelfWidth - widths[books_ith],
                        heights[books_ith]
                        )

                result = min(we_keep, move_on)

                records[key] = result
                return result

        result = sub_min_height(0,0, shelfWidth, 0)
        # print(records)
        return result


def main():
    solu = Solution()

    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
    shelfWidth = 4
    answer = solu.minHeightShelves(books, shelfWidth)
    print(answer)
    

if __name__ == "__main__":
    main()

