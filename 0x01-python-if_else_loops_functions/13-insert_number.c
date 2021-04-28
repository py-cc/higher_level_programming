#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *temp;
  listint_t *new;
  int num = 0;
  int i, j = 0;

  if(head == NULL)
    return NULL;

  temp = *head;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
      return (NULL);

	new->n = number;

  while(head != NULL)
  {
      num = temp->n;
      if(num < number)
      {
		  temp = temp->next;
          j++;
		  continue;
      }
	  break;
  }
  temp = *head;

  for (i = 1; i < j; i++)
  {
	if(temp != NULL)
	{
		temp = temp->next;
	}

  }

  new->next = temp->next;
  temp->next = new;

  return (new);
}
