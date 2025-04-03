#include <stdlib.h>
#include <stdio.h>
#include<string.h> 
#define TRUE	1
#define FALSE	0

typedef int Data;

typedef struct _node
{
	Data data;
	struct _node* next;
	struct _node* prev;
} Node;

typedef struct _dlDeque
{
	Node* head;
	Node* tail;
	Data Qsize;
} DLDeque;

typedef DLDeque Deque;

void DequeInit(Deque* pdeq);
int DQIsEmpty(Deque* pdeq);

void DQAddFirst(Deque* pdeq, Data data);
void DQAddLast(Deque* pdeq, Data data);

Data DQRemoveFirst(Deque* pdeq);
Data DQRemoveLast(Deque* pdeq);

Data DQGetFirst(Deque* pdeq);
Data DQGetLast(Deque* pdeq);

void DequeInit(Deque* pdeq)
{
	pdeq->head = NULL;
	pdeq->tail = NULL;
	pdeq->Qsize = 0;
}
int DQIsEmpty(Deque* pdeq)
{
	if (pdeq->head == NULL)
		return 1;
	else
		return 0;
}
void DQAddFirst(Deque* pdeq, Data data)
{
	Node* newNode;
	newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = pdeq->head;
	if (DQIsEmpty(pdeq))
		pdeq->tail = newNode;
	else
		pdeq->head->prev = newNode;
	newNode->prev = NULL;
	pdeq->head = newNode;
	(pdeq->Qsize)++;
}
void DQAddLast(Deque* pdeq, Data data)
{
	Node* newNode;
	newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->prev = pdeq->tail;
	if (DQIsEmpty(pdeq))
		pdeq->head = newNode;
	else
		pdeq->tail->next = newNode;
	newNode->next = NULL;
	pdeq->tail = newNode;
	(pdeq->Qsize)++;
}
Data DQRemoveFirst(Deque* pdeq)
{
	Node* temp;
	Data rdata;
	if (DQIsEmpty(pdeq))
		return -1;
	temp = pdeq->head;
	rdata = temp->data;
	pdeq->head = temp->next;
	free(temp);
	if (pdeq->head == NULL)
		pdeq->tail = NULL;
	else
		pdeq->head->prev = NULL;
	(pdeq->Qsize)--;
	return rdata;
}
Data DQRemoveLast(Deque* pdeq)
{
	Node* temp = pdeq->tail;
	Data rdata;
	if (DQIsEmpty(pdeq))
		return -1;
	rdata = pdeq->tail->data;

	pdeq->tail = pdeq->tail->prev;

	free(temp);

	if (pdeq->tail == NULL)
		pdeq->head = NULL;
	else
		pdeq->tail->next = NULL;
	(pdeq->Qsize)--;
	return rdata;
}
Data DQGetFirst(Deque* pdeq)
{
	if (DQIsEmpty(pdeq))
		return -1;
	return pdeq->head->data;
}
Data DQGetLast(Deque* pdeq)
{
	if (DQIsEmpty(pdeq))
		return -1;
	return pdeq->tail->data;
}
Data getSize(Deque* pdeq)
{
	return pdeq->Qsize;
}
int main()
{
	Deque q;
	DequeInit(&q);
	int N;
	int M;
	int cnt = 0;
	char input [11];
	
	scanf("%d", &N);
	cnt = N;
	int output[10000] = {0};
	int j = 0;
	for (int i = 0; i < N; i++)
	{
		scanf("%s", input);
		if (strcmp(input, "push_back") == 0)
		{			
			cnt--;
			scanf("%d", &M);
			DQAddLast(&q, M);			
		}
		else if (strcmp(input, "push_front") == 0)
		{
			cnt--;
			scanf("%d", &M);
			DQAddFirst(&q, M);
		}
		else if (strcmp(input, "front")==0)
		{
			output[j++] = DQGetFirst(&q);
		}
		else if (strcmp(input, "back")==0)
		{
			output[j++] = DQGetLast(&q);
		}
		else if (strcmp(input, "empty")==0)
		{
			output[j++] = DQIsEmpty(&q);
		}
		else if (strcmp(input, "size")==0)
		{
			output[j++] = getSize(&q);
		}
		else if (strcmp(input, "pop_front")==0)
		{
			output[j++] = DQRemoveFirst(&q);
		}
		else if (strcmp(input, "pop_back")==0)
		{
			output[j++] = DQRemoveLast(&q);
		}
	}
	int i;
	for (i = 0; i < cnt-1; i++)
	{
		printf("%d\n", output[i]);
	}
	printf("%d", output[i]);
}