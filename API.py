{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "TwitterHTTPError",
     "evalue": "Twitter sent status 401 for URL: 1.1/statuses/home_timeline.json using parameters: (oauth_consumer_key=1083076687-Fp3KjH88VaGevgox05aPu80knZgkq8uQUHvlbSJ&oauth_nonce=18242655319483149816&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1564985368&oauth_token=7o4ZAwwO3VPArcVbS3wtZUA32&oauth_version=1.0&oauth_signature=JSGpl6FC3FZ9a8aSWD1WayiVZoA%3D)\ndetails: {'errors': [{'code': 89, 'message': 'Invalid or expired token.'}]}",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mHTTPError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m~/Twitter/twitter/api.py\u001b[0m in \u001b[0;36m_handle_response\u001b[0;34m(self, req, uri, arg_data, _timeout)\u001b[0m\n\u001b[1;32m    340\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 341\u001b[0;31m             \u001b[0mhandle\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0murllib_request\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    342\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mhandle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mheaders\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Content-Type'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m'image/jpeg'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'image/png'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/urllib/request.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[1;32m    221\u001b[0m         \u001b[0mopener\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_opener\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 222\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mopener\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    223\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/urllib/request.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[1;32m    530\u001b[0m             \u001b[0mmeth\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprocessor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 531\u001b[0;31m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmeth\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    532\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/urllib/request.py\u001b[0m in \u001b[0;36mhttp_response\u001b[0;34m(self, request, response)\u001b[0m\n\u001b[1;32m    640\u001b[0m             response = self.parent.error(\n\u001b[0;32m--> 641\u001b[0;31m                 'http', request, response, code, msg, hdrs)\n\u001b[0m\u001b[1;32m    642\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/urllib/request.py\u001b[0m in \u001b[0;36merror\u001b[0;34m(self, proto, *args)\u001b[0m\n\u001b[1;32m    568\u001b[0m             \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mdict\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'default'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'http_error_default'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0morig_args\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 569\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call_chain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    570\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/urllib/request.py\u001b[0m in \u001b[0;36m_call_chain\u001b[0;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[1;32m    502\u001b[0m             \u001b[0mfunc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhandler\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 503\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    504\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/urllib/request.py\u001b[0m in \u001b[0;36mhttp_error_default\u001b[0;34m(self, req, fp, code, msg, hdrs)\u001b[0m\n\u001b[1;32m    648\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mhttp_error_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 649\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mHTTPError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfull_url\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    650\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mHTTPError\u001b[0m: HTTP Error 401: Authorization Required",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mTwitterHTTPError\u001b[0m                          Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-7aa94936da3c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0mtwitter\u001b[0m \u001b[0;34m=\u001b[0m\u001b[0mTwitter\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mauth\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mOAuth\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mck\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mat\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mats\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m#OAuth認証\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m \u001b[0mtimelines\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtwitter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstatuses\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhome_timeline\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mtimeline\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtimelines\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m     tl = '({id}) [{username}]:{text}'.format(\n",
      "\u001b[0;32m~/Twitter/twitter/api.py\u001b[0m in \u001b[0;36m__call__\u001b[0;34m(self, **kwargs)\u001b[0m\n\u001b[1;32m    332\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_handle_response_with_retry\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marg_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_timeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    333\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 334\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_handle_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marg_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_timeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    335\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    336\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_handle_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marg_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_timeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Twitter/twitter/api.py\u001b[0m in \u001b[0;36m_handle_response\u001b[0;34m(self, req, uri, arg_data, _timeout)\u001b[0m\n\u001b[1;32m    365\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    366\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 367\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mTwitterHTTPError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marg_data\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    368\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    369\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_handle_response_with_retry\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muri\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0marg_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_timeout\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTwitterHTTPError\u001b[0m: Twitter sent status 401 for URL: 1.1/statuses/home_timeline.json using parameters: (oauth_consumer_key=1083076687-Fp3KjH88VaGevgox05aPu80knZgkq8uQUHvlbSJ&oauth_nonce=18242655319483149816&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1564985368&oauth_token=7o4ZAwwO3VPArcVbS3wtZUA32&oauth_version=1.0&oauth_signature=JSGpl6FC3FZ9a8aSWD1WayiVZoA%3D)\ndetails: {'errors': [{'code': 89, 'message': 'Invalid or expired token.'}]}"
     ]
    }
   ],
   "source": [
    "import config\n",
    "import json\n",
    "from twitter import *\n",
    "\n",
    "ck = \"7o4ZAwwO3VPArcVbS3wtZUA32\"\n",
    "cs = \"cOnodu14HZaynR5N4cM2tzsoKnmRxGTBJ0ZOsJkXBcpmxEHZ7Y\"\n",
    "at = \"1083076687-Fp3KjH88VaGevgox05aPu80knZgkq8uQUHvlbSJ\"\n",
    "ats = \"KJJGoiKIjkTMaTY4bfyrzaBX98VaYYCOkgENwrC2vwqNy\"\n",
    "twitter =Twitter(auth=OAuth(ck, cs, at, ats))  #OAuth認証\n",
    "\n",
    "timelines = twitter.statuses.home_timeline()\n",
    "for timeline in timelines:\n",
    "    tl = '({id}) [{username}]:{text}'.format(\n",
    "    id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])\n",
    "    print (tl)"
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
   "display_name": "tf-gpu",
   "language": "python",
   "name": "tf-gpu"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
