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

	temp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
/* en caso de que ingrese en la primera posicion*/
	if (*head == NULL || temp->n > new->n)
	{
		new->next = *head;
		(*head) = new;
		return (new);
	}

	while (temp->next != NULL)
	{
		if ((temp->next->n > new->n && temp->n < new->n) || new->n == temp->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}
