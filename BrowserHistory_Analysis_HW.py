{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6599, 2)"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(r'F:\\UMBC DATA SCIENE SPRING 21\\601\\HW WEEK5\\history_cleaned-1.csv')\n",
    "df.shape"
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
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>domain</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-02-20 19:03:38</td>\n",
       "      <td>piazza.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-02-20 19:03:14</td>\n",
       "      <td>piazza.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-02-20 19:02:36</td>\n",
       "      <td>piazza.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-02-20 19:02:34</td>\n",
       "      <td>piazza.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-02-20 19:02:33</td>\n",
       "      <td>piazza.com</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                  Time      domain\n",
       "0  2021-02-20 19:03:38  piazza.com\n",
       "1  2021-02-20 19:03:14  piazza.com\n",
       "2  2021-02-20 19:02:36  piazza.com\n",
       "3  2021-02-20 19:02:34  piazza.com\n",
       "4  2021-02-20 19:02:33  piazza.com"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>domain</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>6594</th>\n",
       "      <td>2020-12-02 21:36:48</td>\n",
       "      <td>webauth.umbc.edu</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6595</th>\n",
       "      <td>2020-12-02 21:35:59</td>\n",
       "      <td>webauth.umbc.edu</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6596</th>\n",
       "      <td>2020-12-02 08:29:09</td>\n",
       "      <td>www.united.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6597</th>\n",
       "      <td>2020-11-30 07:15:37</td>\n",
       "      <td>cgifederal.secure.force.com</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6598</th>\n",
       "      <td>2020-11-28 22:43:31</td>\n",
       "      <td>asi.payumoney.com</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Time                       domain\n",
       "6594  2020-12-02 21:36:48             webauth.umbc.edu\n",
       "6595  2020-12-02 21:35:59             webauth.umbc.edu\n",
       "6596  2020-12-02 08:29:09               www.united.com\n",
       "6597  2020-11-30 07:15:37  cgifederal.secure.force.com\n",
       "6598  2020-11-28 22:43:31            asi.payumoney.com"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Time      object\n",
       "domain    object\n",
       "dtype: object"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# time column is string and string date is starting with YYYY, so I can do string compares\n",
    "sum(df['Time'] < '1900') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# I filter and get a copy, so I will not work on a slice, this will be a new dataframe. (essentially losing 1900 data points)\n",
    "df = df[df.Time > '1900'].copy() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Time'] = pd.to_datetime(df['Time'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "www.google.com                               1361\n",
       "www.youtube.com                               368\n",
       "blackboard.umbc.edu                           284\n",
       "mail.google.com                               267\n",
       "colab.research.google.com                     253\n",
       "www.amazon.com                                231\n",
       "github.com                                    229\n",
       "www.w3schools.com                             149\n",
       "www.facebook.com                              129\n",
       "drive.google.com                              125\n",
       "webauth.umbc.edu                              103\n",
       "my3.my.umbc.edu                                87\n",
       "stackoverflow.com                              83\n",
       "piazza.com                                     68\n",
       "www.linkedin.com                               60\n",
       "mdmom.org                                      59\n",
       "accounts.google.com                            59\n",
       "careers.compassgroupcareers.com                58\n",
       "qualityinteractions.contentcontroller.com      54\n",
       "localhost:8888                                 50\n",
       "umbc-csm.symplicity.com                        46\n",
       "scikit-learn.org                               44\n",
       "scholar.google.com                             40\n",
       "www.espn.com                                   39\n",
       "docs.google.com                                38\n",
       "gitlab.com                                     35\n",
       "www.xfinity.com                                31\n",
       "towardsdatascience.com                         31\n",
       "www.etsy.com                                   28\n",
       "music.youtube.com                              28\n",
       "umbc2021springfair.vfairs.com                  26\n",
       "www.googleadservices.com                       26\n",
       "umbc.webex.com                                 25\n",
       "www.kaggle.com                                 25\n",
       "my.umbc.edu                                    23\n",
       "www.infosys.com                                23\n",
       "www.citationmachine.net                        22\n",
       "us.bbcollab.com                                22\n",
       "www.paypal.com                                 22\n",
       "watch.tatasky.com                              20\n",
       "www.nap.edu                                    20\n",
       "www.onlinebanking.pnc.com                      20\n",
       "clickserve.dartsearch.net                      20\n",
       "www.hotstar.com                                19\n",
       "oauth.xfinity.com                              18\n",
       "www.instagram.com                              18\n",
       "localhost:8889                                 18\n",
       "www.cbs.com                                    17\n",
       "chrome.google.com                              17\n",
       "myaccount.google.com                           17\n",
       "Name: domain, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['domain'].value_counts()[:50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# top 10 sites that I visisted\n",
    "df['domain'].value_counts()[:10].plot(kind='bar')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Time\n",
       "0     110\n",
       "1       2\n",
       "2      70\n",
       "3      48\n",
       "4       8\n",
       "6       5\n",
       "7       3\n",
       "8       9\n",
       "9      74\n",
       "10    335\n",
       "11    569\n",
       "12    628\n",
       "13    657\n",
       "14    519\n",
       "15    773\n",
       "16    379\n",
       "17    465\n",
       "18    773\n",
       "19    458\n",
       "20    351\n",
       "21    117\n",
       "22    149\n",
       "23     97\n",
       "Name: domain, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hourly_counts = df.groupby(df.Time.dt.hour).domain.size()\n",
    "hourly_counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Time'>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "hourly_counts.plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>domain</th>\n",
       "      <th>Day</th>\n",
       "      <th>DayIndex</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-02-20 19:03:38</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-02-20 19:03:14</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-02-20 19:02:36</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-02-20 19:02:34</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-02-20 19:02:33</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Time      domain       Day  DayIndex\n",
       "0 2021-02-20 19:03:38  piazza.com  Saturday         5\n",
       "1 2021-02-20 19:03:14  piazza.com  Saturday         5\n",
       "2 2021-02-20 19:02:36  piazza.com  Saturday         5\n",
       "3 2021-02-20 19:02:34  piazza.com  Saturday         5\n",
       "4 2021-02-20 19:02:33  piazza.com  Saturday         5"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Day'] = [ d.day_name() for d in df['Time']]\n",
    "df['DayIndex'] = [ d.dayofweek for d in df['Time']]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Tuesday      1596\n",
       "Friday        989\n",
       "Thursday      911\n",
       "Saturday      875\n",
       "Wednesday     835\n",
       "Sunday        721\n",
       "Monday        672\n",
       "Name: Day, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Day'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     672\n",
       "1    1596\n",
       "2     835\n",
       "3     911\n",
       "4     989\n",
       "5     875\n",
       "6     721\n",
       "Name: DayIndex, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "days_sorted = df['DayIndex'].value_counts().sort_index()\n",
    "days_sorted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX0AAAD4CAYAAAAAczaOAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8vihELAAAACXBIWXMAAAsTAAALEwEAmpwYAAATAklEQVR4nO3df6zd933X8edrNnXTRVGT+SYytsEe8krtULrm1ks7DTrCFEOrOhKL5EhdLQgyRN5YYajEq7QgJEsRlP0oLJG8NtSFEmOVjpiNbI0MoWLL4t20WR0783KZs/jWbnyzqFs2Jhd7b/4436qH23Pte8+5Psfe5/mQrPP9vr+f7/m+r2W97sef8z3npKqQJLXhOybdgCRpfAx9SWqIoS9JDTH0Jakhhr4kNWT1pBu4krVr19amTZsm3YYkXVeee+6516pqamH9mg/9TZs2MTMzM+k2JOm6kuT3BtVd3pGkhhj6ktQQQ1+SGmLoS1JDDH1JasgVQz/JY0nOJ3lhQf3HkpxKciLJv+yr70sy2x27u69+R5Lj3bFPJMnK/iiSpCtZykz/08CO/kKSHwR2Au+oqm3Ax7v6VmAXsK0755Ekq7rTHgX2AFu6P//fc0qSrr4rhn5VfRF4fUH5AeDhqrrQjTnf1XcCh6rqQlWdBmaB7UnWATdV1TPV+yznzwD3rNDPIElaomHX9L8H+IEkzyb5n0ne3dXXA2f6xs11tfXd9sL6QEn2JJlJMjM/Pz9ki5KkhYZ9R+5q4GbgTuDdwOEk3w0MWqevy9QHqqoDwAGA6enpZr7lZdODv3xVn//lh99/VZ9f0rVv2Jn+HPD56jkG/Cmwtqtv7Bu3ATjb1TcMqEuSxmjY0P8vwN8ASPI9wJuA14AjwK4ka5JspveC7bGqOge8keTO7q6dDwNPjNq8JGl5rri8k+Rx4H3A2iRzwEPAY8Bj3W2c3wB2dy/QnkhyGDgJXAT2VtWl7qkeoHcn0A3Ak90fSdIYXTH0q+q+RQ59aJHx+4H9A+ozwO3L6k6StKJ8R64kNcTQl6SGGPqS1BBDX5IaYuhLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ15Iqhn+SxJOe7r0ZceOyfJqkka/tq+5LMJjmV5O6++h1JjnfHPtF9V64kaYyWMtP/NLBjYTHJRuCHgFf6aluBXcC27pxHkqzqDj8K7KH3ZelbBj2nJOnqumLoV9UXgdcHHPoZ4KNA9dV2Aoeq6kJVnQZmge1J1gE3VdUz3Reofwa4Z9TmJUnLM9SafpIPAl+tqt9acGg9cKZvf66rre+2F9YXe/49SWaSzMzPzw/ToiRpgGWHfpK3AB8DfmrQ4QG1ukx9oKo6UFXTVTU9NTW13BYlSYtYPcQ5fwnYDPxW91rsBuBLSbbTm8Fv7Bu7ATjb1TcMqEuSxmjZM/2qOl5Vt1bVpqraRC/Q31VVXwOOALuSrEmymd4Ltseq6hzwRpI7u7t2Pgw8sXI/hiRpKZZyy+bjwDPA25LMJbl/sbFVdQI4DJwEfgXYW1WXusMPAJ+k9+Lu/waeHLF3SdIyXXF5p6ruu8LxTQv29wP7B4ybAW5fZn+SpBXkO3IlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1BBDX5IaYuhLUkMMfUlqiKEvSQ0x9CWpIUv5usTHkpxP8kJf7V8l+e0kX0nyi0ne2ndsX5LZJKeS3N1XvyPJ8e7YJ7rvypUkjdFSZvqfBnYsqD0F3F5V7wB+B9gHkGQrsAvY1p3zSJJV3TmPAnvofVn6lgHPKUm6yq4Y+lX1ReD1BbUvVNXFbvc3gA3d9k7gUFVdqKrT9L4EfXuSdcBNVfVMVRXwGeCeFfoZJElLtBJr+n8PeLLbXg+c6Ts219XWd9sL6wMl2ZNkJsnM/Pz8CrQoSYIRQz/Jx4CLwGe/WRowrC5TH6iqDlTVdFVNT01NjdKiJKnP6mFPTLIb+ABwV7dkA70Z/Ma+YRuAs119w4C6JGmMhprpJ9kB/DPgg1X1f/oOHQF2JVmTZDO9F2yPVdU54I0kd3Z37XwYeGLE3iVJy3TFmX6Sx4H3AWuTzAEP0btbZw3wVHfn5W9U1T+sqhNJDgMn6S377K2qS91TPUDvTqAb6L0G8CSSpLG6YuhX1X0Dyp+6zPj9wP4B9Rng9mV1J0laUb4jV5IaYuhLUkMMfUlqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpyxdBP8liS80le6KvdkuSpJC91jzf3HduXZDbJqSR399XvSHK8O/aJ7rtyJUljtJSZ/qeBHQtqDwJHq2oLcLTbJ8lWYBewrTvnkSSrunMeBfbQ+7L0LQOeU5J0lV0x9Kvqi8DrC8o7gYPd9kHgnr76oaq6UFWngVlge5J1wE1V9UxVFfCZvnMkSWMy7Jr+bVV1DqB7vLWrrwfO9I2b62rru+2F9YGS7Ekyk2Rmfn5+yBYlSQutXuHnG7ROX5epD1RVB4ADANPT04uOk/Qtmx785av6/C8//P6r+vwaj2Fn+q92SzZ0j+e7+hywsW/cBuBsV98woC5JGqNhQ/8IsLvb3g080VfflWRNks30XrA91i0BvZHkzu6unQ/3nSNJGpMrLu8keRx4H7A2yRzwEPAwcDjJ/cArwL0AVXUiyWHgJHAR2FtVl7qneoDenUA3AE92fyRJY3TF0K+q+xY5dNci4/cD+wfUZ4Dbl9WdJGlF+Y5cSWqIoS9JDTH0Jakhhr4kNcTQl6SGGPqS1JCV/hgG6brlxxioBc70Jakhhr4kNcTQl6SGuKYv6Zrgayrj4Uxfkhpi6EtSQwx9SWqIoS9JDfGFXK0YX4iTrn3O9CWpISOFfpJ/nOREkheSPJ7kzUluSfJUkpe6x5v7xu9LMpvkVJK7R29fkrQcQ4d+kvXAPwKmq+p2YBWwC3gQOFpVW4Cj3T5JtnbHtwE7gEeSrBqtfUnScoy6vLMauCHJauAtwFlgJ3CwO34QuKfb3gkcqqoLVXUamAW2j3h9SdIyDB36VfVV4OPAK8A54A+q6gvAbVV1rhtzDri1O2U9cKbvKea62rdJsifJTJKZ+fn5YVuUJC0wyvLOzfRm75uBPw98Z5IPXe6UAbUaNLCqDlTVdFVNT01NDduiJGmBUZZ3/iZwuqrmq+r/Ap8H3gu8mmQdQPd4vhs/B2zsO38DveUgSdKYjBL6rwB3JnlLkgB3AS8CR4Dd3ZjdwBPd9hFgV5I1STYDW4BjI1xfkrRMQ785q6qeTfI54EvAReDLwAHgRuBwkvvp/WK4txt/Islh4GQ3fm9VXRqxf0nSMoz0jtyqegh4aEH5Ar1Z/6Dx+4H9o1xTkjQ835ErSQ0x9CWpIYa+JDXE0JekhvjRypK0Aq6XjxZ3pi9JDTH0Jakhhr4kNcTQl6SGGPqS1BBDX5Ia8mfuls3r5bYpSZoEZ/qS1BBDX5IaYuhLUkMMfUlqiKEvSQ0ZKfSTvDXJ55L8dpIXk7wnyS1JnkryUvd4c9/4fUlmk5xKcvfo7UuSlmPUmf7PAb9SVX8Z+Kv0vhj9QeBoVW0Bjnb7JNkK7AK2ATuAR5KsGvH6kqRlGDr0k9wE/DXgUwBV9Y2q+jqwEzjYDTsI3NNt7wQOVdWFqjoNzALbh72+JGn5RpnpfzcwD/y7JF9O8skk3wncVlXnALrHW7vx64EzfefPdbVvk2RPkpkkM/Pz8yO0KEnqN0rorwbeBTxaVd8L/DHdUs4iMqBWgwZW1YGqmq6q6ampqRFalCT1GyX054C5qnq22/8cvV8CryZZB9A9nu8bv7Hv/A3A2RGuL0lapqFDv6q+BpxJ8raudBdwEjgC7O5qu4Enuu0jwK4ka5JsBrYAx4a9viRp+Ub9wLUfAz6b5E3A7wJ/l94vksNJ7gdeAe4FqKoTSQ7T+8VwEdhbVZdGvL4kaRlGCv2qeh6YHnDorkXG7wf2j3JNSdLwfEeuJDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWqIoS9JDTH0Jakhhr4kNWTk0E+yKsmXk/xSt39LkqeSvNQ93tw3dl+S2SSnktw96rUlScuzEjP9Hwde7Nt/EDhaVVuAo90+SbYCu4BtwA7gkSSrVuD6kqQlGin0k2wA3g98sq+8EzjYbR8E7umrH6qqC1V1GpgFto9yfUnS8ow60/9Z4KPAn/bVbquqcwDd461dfT1wpm/cXFf7Nkn2JJlJMjM/Pz9ii5Kkbxo69JN8ADhfVc8t9ZQBtRo0sKoOVNV0VU1PTU0N26IkaYHVI5z7/cAHk/xt4M3ATUn+A/BqknVVdS7JOuB8N34O2Nh3/gbg7AjXlyQt09Az/araV1UbqmoTvRdo/3tVfQg4Auzuhu0Gnui2jwC7kqxJshnYAhwbunNJ0rKNMtNfzMPA4ST3A68A9wJU1Ykkh4GTwEVgb1VdugrXlyQtYkVCv6qeBp7utn8fuGuRcfuB/StxTUnS8vmOXElqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWrI0KGfZGOS/5HkxSQnkvx4V78lyVNJXuoeb+47Z1+S2SSnkty9Ej+AJGnpRpnpXwR+oqreDtwJ7E2yFXgQOFpVW4Cj3T7dsV3ANmAH8EiSVaM0L0lanqFDv6rOVdWXuu03gBeB9cBO4GA37CBwT7e9EzhUVReq6jQwC2wf9vqSpOVbkTX9JJuA7wWeBW6rqnPQ+8UA3NoNWw+c6TttrqsNer49SWaSzMzPz69Ei5IkViD0k9wI/GfgI1X1h5cbOqBWgwZW1YGqmq6q6ampqVFblCR1Rgr9JH+OXuB/tqo+35VfTbKuO74OON/V54CNfadvAM6Ocn1J0vKMcvdOgE8BL1bVT/cdOgLs7rZ3A0/01XclWZNkM7AFODbs9SVJy7d6hHO/H/gR4HiS57vaTwIPA4eT3A+8AtwLUFUnkhwGTtK782dvVV0a4fqSpGUaOvSr6n8xeJ0e4K5FztkP7B/2mpKk0fiOXElqiKEvSQ0x9CWpIYa+JDXE0Jekhhj6ktQQQ1+SGmLoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIYY+pLUEENfkhpi6EtSQwx9SWrI2EM/yY4kp5LMJnlw3NeXpJaNNfSTrAJ+HvhbwFbgviRbx9mDJLVs3DP97cBsVf1uVX0DOATsHHMPktSsVNX4Lpb8MLCjqv5+t/8jwPdV1Y8uGLcH2NPtvg04dRXbWgu8dhWf/2q6nnsH+580+5+sq93/X6yqqYXF1VfxgoNkQO3bfutU1QHgwNVvB5LMVNX0OK610q7n3sH+J83+J2tS/Y97eWcO2Ni3vwE4O+YeJKlZ4w793wS2JNmc5E3ALuDImHuQpGaNdXmnqi4m+VHgV4FVwGNVdWKcPQwwlmWkq+R67h3sf9Lsf7Im0v9YX8iVJE2W78iVpIYY+pLUkOZCP0kl+fd9+6uTzCf5pUn2tVRJvivJ892fryX5at/+mybd3+Uk+ZkkH+nb/9Ukn+zb/9dJ/slEmruMy/ydfz3JyUn3t1xJLvX9PM8n2TTpnq4kyceSnEjyla7n75t0T8txLfU/7vv0rwV/DNye5Iaq+hPgh4CvTrinJauq3wfeCZDknwN/VFUfn2RPy/DrwL3Azyb5DnpvTrmp7/h7gY9MoK/LWuzvvAvL62KysMCfVNU7J93EUiV5D/AB4F1VdSHJWuCanuD0u9b6b26m33kSeH+3fR/w+AR7acmv0Qt2gG3AC8AbSW5OsgZ4O/DlSTU3pFVJfqGbxX0hyQ2TbujPoHXAa1V1AaCqXquqs0l+KslvJnkhyYEkg978eS1YrP+Xu18AJJlO8vQ4mmk19A8Bu5K8GXgH8OyE+2lCVZ0FLib5C/TC/xl6f/fvAaaBr3SfyXQ92QL8fFVtA74O/J3JtrMkN/Qt7fzipJtZgi8AG5P8TpJHkvz1rv5vq+rdVXU7cAO92fS1aLH+J6LF5R2q6ivdf83vA/7bhNtpzTdn++8FfhpY323/Ab3ln+vN6ap6vtt+Dtg0uVaW7Lpa3qmqP0pyB/ADwA8C/6n7WPY3knwUeAtwC3AC+K+T63Swy/Q/EU2GfucI8HHgfcB3TbaVpvw6vZD/K/SWd84APwH8IfDYBPsa1oW+7Uv0ZpxaYVV1CXgaeDrJceAf0Ptf+nRVnelea3nz5Dq8vAH97wYu8q3VlrH13uryDvQC5l9U1fFJN9KYX6P33/DXq+pSVb0OvJXeEs8zk2xM16Ykb0uypa/0Tr71ybuvJbkR+OGxN7ZEi/T/e8DLwB1dbWzLgs3O9KtqDvi5SffRoOP07tr5jwtqN1bV9fwxubp6bgT+TZK30psdz9L76PWv0/u38zK9z/W6Vi3W/9uBTyX5Scb4uqIfwyBJDWl5eUeSmmPoS1JDDH1JaoihL0kNMfQlqSGGviQ1xNCXpIb8P9SQTklKpJWzAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "days_sorted.plot.bar()\n",
    "plt.xticks(days_sorted.index, ['M', 'T', 'W','Th', 'F', 'Sa', 'Su'], rotation=0)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>domain</th>\n",
       "      <th>Day</th>\n",
       "      <th>DayIndex</th>\n",
       "      <th>isWeekend</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-02-20 19:03:38</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-02-20 19:03:14</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-02-20 19:02:36</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-02-20 19:02:34</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-02-20 19:02:33</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Time      domain       Day  DayIndex  isWeekend\n",
       "0 2021-02-20 19:03:38  piazza.com  Saturday         5       True\n",
       "1 2021-02-20 19:03:14  piazza.com  Saturday         5       True\n",
       "2 2021-02-20 19:02:36  piazza.com  Saturday         5       True\n",
       "3 2021-02-20 19:02:34  piazza.com  Saturday         5       True\n",
       "4 2021-02-20 19:02:33  piazza.com  Saturday         5       True"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def is_weekend(day): \n",
    "    return day in ['Saturday', 'Sunday']\n",
    "\n",
    "\n",
    "df['isWeekend'] = [ is_weekend(i) for i in df['Day']]\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "weekend = df[ df['isWeekend'] == True ]\n",
    "\n",
    "weekday = df[ df['isWeekend'] == False ]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Time</th>\n",
       "      <th>domain</th>\n",
       "      <th>Day</th>\n",
       "      <th>DayIndex</th>\n",
       "      <th>isWeekend</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-02-20 19:03:38</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-02-20 19:03:14</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-02-20 19:02:36</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-02-20 19:02:34</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-02-20 19:02:33</td>\n",
       "      <td>piazza.com</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>5</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 Time      domain       Day  DayIndex  isWeekend\n",
       "0 2021-02-20 19:03:38  piazza.com  Saturday         5       True\n",
       "1 2021-02-20 19:03:14  piazza.com  Saturday         5       True\n",
       "2 2021-02-20 19:02:36  piazza.com  Saturday         5       True\n",
       "3 2021-02-20 19:02:34  piazza.com  Saturday         5       True\n",
       "4 2021-02-20 19:02:33  piazza.com  Saturday         5       True"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weekend.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "www.google.com               1051\n",
       "www.youtube.com               276\n",
       "blackboard.umbc.edu           250\n",
       "colab.research.google.com     243\n",
       "mail.google.com               213\n",
       "Name: domain, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weekday['domain'].value_counts()[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "www.google.com     310\n",
       "www.amazon.com     168\n",
       "www.youtube.com     92\n",
       "github.com          64\n",
       "mail.google.com     54\n",
       "Name: domain, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "weekend['domain'].value_counts()[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def show_stats(df, color, alpha=1):\n",
    "    hourly_counts = df.groupby(df.Time.dt.hour).domain.size()\n",
    "    \n",
    "    # fill in the missing hours\n",
    "    for h in range(24):\n",
    "        if h not in hourly_counts:\n",
    "            hourly_counts[h]=0 # I initially didn't do this and hours were not lining up\n",
    "            \n",
    "    hourly_counts.sort_index().plot.bar(color=color, alpha=alpha)\n",
    "    plt.ylim([0, 1300])\n",
    "\n",
    "    \n",
    "show_stats(weekend, 'red', 1)\n",
    "    \n",
    "show_stats(weekday, 'blue', 0.5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# be skeptical about your data!\n",
    "# am I on computer a lot more on the weekdays \n",
    "# or it shows more simply becasue there are more weekdays "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def show_stats(df, color, alpha=1, title='', y_lim = None):\n",
    "    hourly_counts = df.groupby(df.Time.dt.hour).domain.size()\n",
    "    \n",
    "    days_counts = df.Time.dt.date.nunique()\n",
    "    \n",
    "    # fill in the missing hours\n",
    "    for h in range(24):\n",
    "        if h not in hourly_counts:\n",
    "            hourly_counts[h]=0 # I initially didn't do this and hours were not lining up\n",
    "        else: \n",
    "            hourly_counts[h] = hourly_counts[h] * 100.0 /  days_counts # I multiplied by 100.0 to make it float and also not to loose decimals\n",
    "            \n",
    "    hourly_counts.sort_index().plot.bar(color=color, alpha=alpha, title=title)\n",
    "    \n",
    "    if y_lim != None:\n",
    "        plt.ylim(y_lim)\n",
    "    plt.show()\n",
    "\n",
    "\n",
    "    \n",
    "y_lim=[0, 1800]\n",
    "show_stats(weekend, 'red', 1, 'Weekend', y_lim=y_lim)\n",
    "    \n",
    "show_stats(weekday, 'blue', 0.5, 'Weekday', y_lim=y_lim)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "www.google.com                               1361\n",
       "www.youtube.com                               368\n",
       "blackboard.umbc.edu                           284\n",
       "mail.google.com                               267\n",
       "colab.research.google.com                     253\n",
       "www.amazon.com                                231\n",
       "github.com                                    229\n",
       "www.w3schools.com                             149\n",
       "www.facebook.com                              129\n",
       "drive.google.com                              125\n",
       "webauth.umbc.edu                              103\n",
       "my3.my.umbc.edu                                87\n",
       "stackoverflow.com                              83\n",
       "piazza.com                                     68\n",
       "www.linkedin.com                               60\n",
       "mdmom.org                                      59\n",
       "accounts.google.com                            59\n",
       "careers.compassgroupcareers.com                58\n",
       "qualityinteractions.contentcontroller.com      54\n",
       "localhost:8888                                 50\n",
       "umbc-csm.symplicity.com                        46\n",
       "scikit-learn.org                               44\n",
       "scholar.google.com                             40\n",
       "www.espn.com                                   39\n",
       "docs.google.com                                38\n",
       "gitlab.com                                     35\n",
       "www.xfinity.com                                31\n",
       "towardsdatascience.com                         31\n",
       "www.etsy.com                                   28\n",
       "music.youtube.com                              28\n",
       "umbc2021springfair.vfairs.com                  26\n",
       "www.googleadservices.com                       26\n",
       "umbc.webex.com                                 25\n",
       "www.kaggle.com                                 25\n",
       "my.umbc.edu                                    23\n",
       "www.infosys.com                                23\n",
       "www.citationmachine.net                        22\n",
       "us.bbcollab.com                                22\n",
       "www.paypal.com                                 22\n",
       "watch.tatasky.com                              20\n",
       "www.nap.edu                                    20\n",
       "www.onlinebanking.pnc.com                      20\n",
       "clickserve.dartsearch.net                      20\n",
       "www.hotstar.com                                19\n",
       "oauth.xfinity.com                              18\n",
       "www.instagram.com                              18\n",
       "localhost:8889                                 18\n",
       "www.cbs.com                                    17\n",
       "chrome.google.com                              17\n",
       "myaccount.google.com                           17\n",
       "Name: domain, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['domain'].value_counts()[:50]"
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
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['domain'] = df['domain'].astype(str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_data_for_domain(val):\n",
    "    return df[ [True if val.lower() in i.lower() else False for i in df['domain'] ]]\n",
    "\n",
    "\n",
    "def show_domain_stats(domain, color='blue', alpha=1):\n",
    "    data = get_data_for_domain(domain)\n",
    "    show_stats(data, color, alpha)\n",
    "    return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "_= show_domain_stats('facebook', 'blue')"
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
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "_ = show_domain_stats('stackover', 'magenta')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "_ = show_domain_stats('netflix', 'red')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "_=show_domain_stats('amazon', 'black')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Based on data, what can we tell about this person?\n",
    "\n",
    "1. Is this a work computer/personal computer?\n",
    "1. Is s/he employed?\n",
    "1. What are his/her interests?\n",
    "1. List any interesting findings"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "answer here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "  1. By above analysis we can say that its a personal computer\n",
    "  2. he is a student as he is visting educational sites.\n",
    "  3. he seems to be shopholic as he seems to visit amazon site frequently. \n",
    "  4. Intrestingly we can say that the person is keeping an routine activity on laptop from 9am to 11pm across all days in a week. He/She is seeking to gain knowledge by visting educational sites. "
   ]
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
