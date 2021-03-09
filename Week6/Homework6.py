{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Homework Week6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. There is a bug in this program. Find, explain & fix.\n",
    "1. Fill the docstrings (python documentation) \n",
    "    * What the function does\n",
    "    * what it expects\n",
    "    * what it returns\n",
    "\n",
    "1. Add a new method to `clear` the ShoppingList class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "items = []\n",
    "\n",
    "class ShoppingList:\n",
    "    \n",
    "    def __init__(self):\n",
    "        \"\"\"\n",
    "        This is a constructor used for inializing the shopping list\n",
    "        This constructor will not take any value as an input\n",
    "        This constructor Will not return any values\n",
    "        \n",
    "        \"\"\"\n",
    "        \n",
    "    def add_item(self, item):\n",
    "        \"\"\"\n",
    "        This Method is meant for adding items into shopping list\n",
    "        This Method will take any value as an input to add into list\n",
    "        This Method Will return count of the items added to shopping list\n",
    "        \"\"\"\n",
    "        items.append(item)\n",
    "        \n",
    "        return len(items)\n",
    "\n",
    "    def remove_item(self, item):\n",
    "        \"\"\"\n",
    "        This Method is meant for removing items from shopping list\n",
    "        This Method will take any value as an input to remove matching element from list\n",
    "        This Method Will return count of the items left in the shopping list\n",
    "        \"\"\"\n",
    "        items.remove(item)\n",
    "        \n",
    "        return len(items)\n",
    "    \n",
    "    def get_items(self):\n",
    "        \"\"\"\n",
    "        This Method is meant for returning list of  items available in the shopping list\n",
    "        This Method won't take any value as an input\n",
    "        \"\"\"\n",
    "        return items\n",
    "    \n",
    "    def clear(self):\n",
    "        \"\"\"\n",
    "              This Method is meant for clearing the items from shopping list\n",
    "              This Method will not take any value as an input\n",
    "              This Method Will not return any values\n",
    "        \"\"\"\n",
    "        items.clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "husband = ShoppingList()\n",
    "wife = ShoppingList()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Added 1 Items To Shopping List\n",
      "Added 2 Items To Shopping List\n"
     ]
    }
   ],
   "source": [
    "print(\"Added \"+str(husband.add_item('ps5'))+\" Items To Shopping List\")\n",
    "print(\"Added \"+str(wife.add_item('dress'))+\" Items To Shopping List\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ps5', 'dress']\n"
     ]
    }
   ],
   "source": [
    "print(husband.get_items())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['ps5', 'dress']\n"
     ]
    }
   ],
   "source": [
    "print(wife.get_items())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
