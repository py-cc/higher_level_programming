#include "lists.h"
#include <stdlib.h>
/**
* insert_node -  inserts a number into a sorted singly linked list.
* @head: pointer to linked list
* @number: num to inserts
* Return: the address of the new node, or NULL if it failed
**/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp;
listint_t *new;
int num = 0;
int i, j = 0;
if (head == NULL)
return (NULL);
temp = *head;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL)
new->n = number;
while (head != NULL)
{
if (temp->next != NULL)
{
num = temp->n;
if (num < number)
{
temp = temp->next;
j++;
continue;
}
break;
}
}
temp = *head;
for (i = 1; i < j; i++)
{
if (temp != NULL)
{
temp = temp->next;
}
}
new->next = temp->next;
temp->next = new;
return (new);
}
